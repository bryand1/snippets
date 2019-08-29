import * as caseActions from "./caseActions";
import * as types from "./actionTypes";
import { cases } from "../../../tools/mockData";

describe("createCaseSuccess", () => {
  it("should create a CREATE_CASE_SUCCESS action", () => {
    const myCase = cases[0];
    const expectedAction = {
      type: types.CREATE_CASE_SUCCESS,
      case: myCase
    };

    // actual
    const action = caseActions.createCaseSuccess(myCase);

    // assert
    expectedAction(action).toEqual(expectedAction);
  });
});
