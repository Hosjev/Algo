import {
  AxiosProxyConfig,
  AxiosRequestConfig,
  Method,
  ResponseType,
} from 'axios'

export interface HttpClientConfig {
  /**
   * debug is set to false by default. When debug is set to `true`,
   *  the API response will data will not be sanitized and response will include
   * `config` and `request` which could be containing sensitive data
   */
  debug?: boolean
  baseUrl?: string
  useFixie?: boolean
  proxy?: string
  timeout?: number
  headers?: object
  auth?: BasicAuthCredentials
  /**
   * Sanitize error responses to remove sensitive data
   */
  sanitizeFields?: string[]
}

interface BasicAuthCredentials {
  username: string
  password: string
}

export interface HttpClientOptions {
  url?: string
  data?: object
  params?: object
  method?: Method
  headers?: object
  timeout?: number
  auth?: BasicAuthCredentials
  maxContentLength?: number
  maxBodyLength?: number
  maxRedirects?: number
  httpAgent?: object
  httpsAgent?: object
  proxy?: AxiosProxyConfig | false
  responseType?: ResponseType
}

export interface HttpClientResponse<T = any> {
  data: T
  status: number
  statusText: string
  headers: object
  config?: AxiosRequestConfig
  request?: object
}
