<template>
  <div>
    <label>主队：
      <select v-model="home">
        <option v-for="team in teams" :key="team.id" :value="team.id">{{ team.name }}</option>
      </select>
    </label>
    <label>客队：
      <select v-model="away">
        <option v-for="team in teams" :key="team.id" :value="team.id">{{ team.name }}</option>
      </select>
    </label>
    <button @click="$emit('startMatch', home, away)">开始模拟</button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      teams: [],
      home: '',
      away: ''
    }
  },
  async mounted() {
    try {
      const { data } = await axios.get('http://127.0.0.1:8000/api/teams')
      this.teams = data
      if (data.length >= 2) {
        this.home = data[0].id
        this.away = data[1].id
      }
    } catch (err) {
      console.error(err)
      alert('获取球队列表失败')
    }
  }
}
</script>