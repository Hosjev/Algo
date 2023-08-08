import axios from 'axios'

let _token
let _accessTokenExpire


const getPerimeterEightOneToken = async () => {
  if (_token && Date.now() - _accessTokenExpire < 3600) return _token

  const { data } = await axios.post(
    `${perimeter81BaseUrl}/v1/auth/authorize`,
    null,
    {
      headers: {
        grantType: 'api_key',
        apiKey: p81NetworkReadAPIKey,
      },
    },
  )

  const { accessToken, accessTokenExpire } = data
  _token = accessToken
  _accessTokenExpire = accessTokenExpire

  return accessToken
}

export const getPerimeterEightOneNetworks = async () => {
  const token = await getPerimeterEightOneToken()

  const { data } = await axios.get(`${perimeter81BaseUrl}/rest/v1/networks`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })

  return data[0].regions.map((item) => item.map((zone) => zone.ip))
}

