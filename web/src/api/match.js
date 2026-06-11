import axios from 'axios'

export async function simulateMatch(homeTeam, awayTeam) {
  const payload = {
    home_team: homeTeam,
    away_team: awayTeam
  }
  const { data } = await axios.post('http://127.0.0.1:8000/api/simulate', payload)
  return data
}