import axios from 'axios'

let _token
let _accessTokenExpire

const perimeter81BaseUrl = 'https://api.perimeter81.com/api'
const p81NetworkReadAPIKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJhZmYzZDEyYjE3MmQ2MGJiNjI2ZjRjMDE5YjExM2U3YiIsImlkIjoiR2lVdFJQN1NkNyIsInNjb3BlcyI6WyJORVRXT1JLX1JFQUQiLCJORVRXT1JLX0hFQUxUSF9SRUFEIl0sInRlbmFudElkIjoiY2hpcHBlciIsImlhdCI6MTY2NzkzMDcwNiwiZXhwIjo0Nzg5OTk0NzA2LCJhdWQiOiJzYWZlci1hdXRoIiwiaXNzIjoiYXV0aC5zYWZlcnNvZnR3YXJlLmNvbSIsInN1YiI6ImNoaXBwZXIifQ.l68AC3c9lnbLIIJ3NSjBU-20ZBYIjh9aVEHIlVFptUA'

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

