// https://www.youtube.com/watch?v=wcRawY6aJaw
function reducer(state, action) {
  switch(action.type) {
    case "toggle-todo":
      return {
        todos: state.todos.map((t, idx) =>
          idx === action.idx ? { ...t, completed: !t.completed } : t
        )
      }
  }
}
