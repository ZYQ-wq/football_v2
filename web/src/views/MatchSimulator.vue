<template>
  <div class="match-simulator">
    <h1>AI Football Simulator</h1>

    <TeamSelector
      v-model:modelValueHome="homeTeam"
      v-model:modelValueAway="awayTeam"
    />

    <button @click="startMatch" :disabled="loading">
      开始模拟
    </button>

    <LoadingPanel v-if="loading" />

    <MatchHeader v-if="result" :score="result.score" />

    <CommentaryPanel v-if="result" :commentary="result.commentary" />
  </div>
</template>

<script setup>
import { ref } from "vue"
import TeamSelector from "../components/TeamSelector.vue"
import MatchHeader from "../components/MatchHeader.vue"
import CommentaryPanel from "../components/CommentaryPanel.vue"
import LoadingPanel from "../components/LoadingPanel.vue"
import { simulateMatch } from "../api/match"

const homeTeam = ref("england")
const awayTeam = ref("france")
const result = ref(null)
const loading = ref(false)

const startMatch = async () => {
  loading.value = true
  try {
    const res = await simulateMatch(homeTeam.value, awayTeam.value)
    result.value = res.data
  } catch (err) {
    console.error(err)
  } finally {
    loading.value = false
  }
}
</script>