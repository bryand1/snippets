import axios from "axios"

export function fetchApp() {
  return function(dispatch) {
    dispatch({type: "FETCH_APP_PENDING"});
    axios.post("/api?action=fetch")
      .then((response) => {
        dispatch({type: "FETCH_APP_FULFILLED", payload: response.data})
        dispatch(progressApp());
      })
      .catch((err) => {
        dispatch({type: "FETCH_APP_REJECTED", payload: err})
      });
  }
}
