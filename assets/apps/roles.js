const app = new Vue({
  el: '#roles-game',
  data: {
    room: 'start',
    message: ''
  },
  methods: {
    goto: function (room) {
      this.room = room;
    },
    game_over: function (message) {
      this.message = message;
    },
    reset: function () {
      this.message = '';
      this.room = 'start';
    }
  }
});