// Use immer in Redux reducer for immutability
import produce from 'immer';

const nextState = produce(baseState, draftState => {
  draftState.push({todo: "New item"});
});

