<template>
  <div id="app">
    <MatchHeader />
    <TeamSelector @startMatch="startMatch" />
    <LoadingPanel v-if="loading" />
    <CommentaryPanel v-if="commentary.length" :lines="commentary" />
    <div v-if="score">最终比分：{{ score }}</div>
  </div>
</template>

<script>
import MatchHeader from './components/MatchHeader.vue'
import TeamSelector from './components/TeamSelector.vue'
import CommentaryPanel from './components/CommentaryPanel.vue'
import LoadingPanel from './components/LoadingPanel.vue'
import { simulateMatch } from './api/match.js'

export default {
  components: { MatchHeader, TeamSelector, CommentaryPanel, LoadingPanel },
  data() {
    return {
      commentary: [],
      score: '',
      loading: false
    }
  },
  methods: {
    async startMatch(homeTeam, awayTeam) {
      this.loading = true
      this.commentary = []
      this.score = ''
      try {
        const res = await simulateMatch(homeTeam, awayTeam)
        this.score = res.score
        // 将 commentary 一条一条滚动显示
        const lines = res.commentary.split('\n')
        for (const line of lines) {
          if (line.trim() === '') continue
          this.commentary.push(line)
          await new Promise(r => setTimeout(r, 800)) // 每条 0.8 秒
        }
      } catch (err) {
        console.error(err)
        alert('比赛模拟失败')
      } finally {
        this.loading = false
      }
    }
  }
}
</script>