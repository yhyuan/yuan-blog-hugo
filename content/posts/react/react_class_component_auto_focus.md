---
title: How to Write a React class component with Radio group which will focus on the radio group 500 ms after each click
date: '2023-07-24'
tags: ['chatgpt', 'react']
draft: false
description: The artical descript how to write a class component with radio group
---

## Introduction

Recently, I need to develop a React class component which will focus on the radio group 500 ms after each click with ChatGPT. 


## Develop
Use the following prompt for chatGPT.
```
write a React class component with radio group which will focus on the radio group 500 ms after each click
```

ChatGPT output: 
Sure! Here's an example of a React class component with a radio group that will focus on the radio group 500 ms after each click:

```javascript
import React from 'react';

class RadioGroupWithFocus extends React.Component {
  constructor(props) {
    super(props);
    this.radioGroupRef = React.createRef();
  }

  handleRadioClick = () => {
    // Set focus on the radio group after 500 ms
    setTimeout(() => {
      this.radioGroupRef.current.focus();
    }, 500);
  };

  render() {
    return (
      <div>
        <label>
          <input type="radio" name="radioGroup" onClick={this.handleRadioClick} />
          Option 1
        </label>
        <label>
          <input type="radio" name="radioGroup" onClick={this.handleRadioClick} />
          Option 2
        </label>
        <label>
          <input type="radio" name="radioGroup" onClick={this.handleRadioClick} />
          Option 3
        </label>
        <label>
          <input type="radio" name="radioGroup" onClick={this.handleRadioClick} />
          Option 4
        </label>
        <label>
          <input type="radio" name="radioGroup" onClick={this.handleRadioClick} />
          Option 5
        </label>
        <div tabIndex={0} ref={this.radioGroupRef}>
          {/* Radio group content */}
        </div>
      </div>
    );
  }
}

export default RadioGroupWithFocus;
```
ChatGPT explanation: 
In this component, we create a radioGroupRef using React.createRef() to reference the ```<div>``` element that wraps the radio group content. The handleRadioClick method is called when any radio button is clicked. It uses setTimeout to set focus on the radio group (```<div>```) after a delay of 500 milliseconds.

This way, when a user clicks on any radio button in the group, the radio group will receive focus after a short delay of 500 ms. You can use this RadioGroupWithFocus component in your application as needed.

## Test
Use the following prompt for chatGPT to write a test for the component.
```
Write a enzyme based test to test this component
```

To test the RadioGroupWithFocus component using Enzyme, we need to install the required dependencies first:
```bash
npm install enzyme enzyme-adapter-react-16 react-test-renderer --save-dev
```
Next, create a test file, e.g., RadioGroupWithFocus.test.js, and write the Enzyme-based test:

```javascript
import React from 'react';
import { mount } from 'enzyme';
import RadioGroupWithFocus from './RadioGroupWithFocus';

describe('RadioGroupWithFocus', () => {
  it('should focus on the radio group after each click', (done) => {
    const wrapper = mount(<RadioGroupWithFocus />);
    const radioGroupDiv = wrapper.find('div[tabIndex]');

    // Simulate a click on the first radio button
    wrapper.find('input[type="radio"]').first().simulate('click');

    // Wait for 500ms and check if the radio group div is focused
    setTimeout(() => {
      expect(document.activeElement).toBe(radioGroupDiv.getDOMNode());
      done();
    }, 500);
  });
});

```

In this test, we use mount from Enzyme to render the RadioGroupWithFocus component. We find the ```<div>``` element with tabIndex (which is our radio group) using the wrapper.find method.

Next, we simulate a click on the first radio button using ```wrapper.find('input[type="radio"]').first().simulate('click')```. This will trigger the handleRadioClick function in the component, which sets a timeout to focus on the radio group after 500 ms.

Finally, we use setTimeout to wait for 500 ms before checking if the radio group (```div```) is focused using document.activeElement. If the focus is on the radio group after the click, the test will pass.

To run the test, you can use your preferred test runner (e.g., Jest) and execute the test file. Make sure you have the correct Enzyme and adapter configuration set up in your testing environment.

## Mock focus function
prompt:
```
please mock focus function in this test and make sure it is called after each click
```

Sure! To mock the focus function and ensure that it is called after each click, we can use Jest's mock functions and Enzyme's simulate method. Here's the updated test:
```javascript
import React from 'react';
import { mount } from 'enzyme';
import RadioGroupWithFocus from './RadioGroupWithFocus';

describe('RadioGroupWithFocus', () => {
  it('should focus on the radio group after each click', () => {
    const focusMock = jest.fn();
    HTMLElement.prototype.focus = focusMock;

    const wrapper = mount(<RadioGroupWithFocus />);
    const radioGroupDiv = wrapper.find('div[tabIndex]');

    // Simulate a click on the first radio button
    wrapper.find('input[type="radio"]').first().simulate('click');

    // Ensure the focus function is called after 500ms
    jest.advanceTimersByTime(500);
    expect(focusMock).toHaveBeenCalledTimes(1);

    // Simulate a click on another radio button
    wrapper.find('input[type="radio"]').at(2).simulate('click');

    // Ensure the focus function is called again after 500ms
    jest.advanceTimersByTime(500);
    expect(focusMock).toHaveBeenCalledTimes(2);
  });
});

```
In this updated test, we use jest.fn() to create a mock function called focusMock. Then, we assign this mock function to the focus prototype of HTMLElement. This will make sure that any call to the focus function is replaced with our mock function.

After simulating a click on the first radio button, we advance the timers by 500ms using jest.advanceTimersByTime(500) to simulate the 500ms delay. Then, we check if the mock function focusMock has been called once using expect(focusMock).toHaveBeenCalledTimes(1).

Next, we simulate a click on another radio button and repeat the process to ensure that the focus function is called again after another 500ms delay.

With this test, we have mocked the focus function and verified that it is called after each click, as intended.

## Conclusion

ChatGPT can successfully create the component code and test code. 