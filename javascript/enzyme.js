import React from "react";
import CustomComponent from "./CustomComponent";
import { shallow } from "enzyme";
import { isMainThread } from "worker_threads";

function renderCustomComponent(args) {
  const defaultProps = {
    label: "MyButton",
    onChange: () => {}
  };

  const props = { ...defaultProps, ...args };
  return shallow(<CustomComponent {...props} />);
}

it("renders button", () => {
  const wrapper = renderCustomComponent();
  expect(wrapper.find("button").length).toBe(1);
  expect(wrapper.find("label").text()).toEqual("MyButton");
});
