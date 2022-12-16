import axios, { AxiosError, AxiosInstance } from 'axios'
import env from 'util/env'
import { sanitizeObject } from 'util/sanitizeObject'
import {
  HttpClientConfig,
  HttpClientOptions,
  HttpClientResponse,
} from './types'

/**
 * Initialize Http client
 *
 * @param {boolean} params.debug - debug is set to false by default. When debug is set to `true`,
 *  the API response will data will not be sanitized and response will include
 * `config` and `request` which could be containing sensitive data
 * @param {string} params.baseUrl - Set a base url
 * @param {boolean} params.useFixie - Use fixie proxy with HttpClient
 * @param {string} params.proxy - setting `proxy` will override `useFixie` config
 * @param {number} params.timeout - in milliseconds
 * @param {Object} params.headers - Http headers
 * @param {Array} params.sanitizeFields - Sanitize error responses to remove sensitive data
 */
function init(params?: HttpClientConfig) {
  const debug = params?.debug || false
  const instance = axios.create()

  if (params?.headers) {
    instance.defaults.headers = params?.headers
  }

  if (params?.timeout) {
    instance.defaults.timeout = params?.timeout
  }

  if (params?.auth) {
    instance.defaults.auth = params?.auth
  }

  if (params?.baseUrl) {
    instance.defaults.baseURL = params?.baseUrl
  }

  setupInterceptor(instance, params?.sanitizeFields, debug)

  return httpMethods(instance)
}

function httpMethods(instance: AxiosInstance) {
  return {
    async get<T = any, R = HttpClientResponse<T>>(
      url: string,
      options?: HttpClientOptions,
    ): Promise<R> {
      return instance.get(url, options)
    },
    async put<T = any, R = HttpClientResponse<T>>(
      url: string,
      data?: object,
      options?: HttpClientOptions,
    ): Promise<R> {
      return instance.put(url, data, options)
    },
    async patch<T = any, R = HttpClientResponse<T>>(
      url: string,
      data?: object,
      options?: HttpClientOptions,
    ): Promise<R> {
      return instance.patch(url, data, options)
    },
    async post<T = any, R = HttpClientResponse<T>>(
      url: string,
      data?: object,
      options?: HttpClientOptions,
    ): Promise<R> {
      return instance.post(url, data, options)
    },
    async delete<T = any, R = HttpClientResponse<T>>(
      url: string,
      options?: HttpClientOptions,
    ): Promise<R> {
      return instance.delete(url, options)
    },
    async request<T = any, R = HttpClientResponse<T>>(
      options: HttpClientOptions,
    ): Promise<R> {
      return instance.request(options)
    },
  }
}

function parseResponse(response, debug: boolean) {
  const { status, statusText, headers, data, ...rest } = response
  const debugData = !debug ? {} : rest

  return { status, statusText, headers, data, ...debugData }
}

function setupInterceptor(
  instance: AxiosInstance,
  sanitizeFields: string[],
  debug: boolean,
) {
  // Add a response interceptor
  instance.interceptors.response.use(
    (response) => {
      // Any status code that lie within the range of 2xx cause this function to trigger
      // Do something with response data
      return parseResponse(response, debug)
    },
    (error) => {
      // Any status codes that falls outside the range of 2xx cause this function to trigger
      // Do something with response error

      let err
      if (!debug) {
        const { response } = error as AxiosError

        // Remove objects that could potentially contain secret keys
        if (response.config) {
          delete response.config
        }

        if (response.request) {
          delete response.request
        }

        err = sanitizeObject(
          { ...error.toJSON(), response },
          sanitizeFields || [],
        )
      }

      return Promise.reject(err || error)
    },
  )
}

const HttpClient = { init }

export default HttpClient
