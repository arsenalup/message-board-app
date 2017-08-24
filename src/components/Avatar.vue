<template>
  <span class="v-avatar" :style="styleSize" :aria-label="alt">
  <span class="v-avatar-text" v-text="name" :style="{background: bg, color: fg}"></span>
  </span>
</template>
<script>
import wc from "word-color"
//alt 传入的用户名
// size 头像尺寸
export default {
	props: ['alt', 'size']

	data()
}
</script>