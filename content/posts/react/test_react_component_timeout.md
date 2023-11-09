---
title: How to Write and Test a React Component with Timeout using ChatGPT
date: '2023-05-25'
tags: ['chatgpt', 'react']
draft: false
description: The artical descript how to test a React component with Timeout function
---

## Introduction

Recently, I need to develop a React component which will render a div after a mouse click. Then, after 1 minute, the div will disappear automatically. 


## Develop
Use the following prompt for chatGPT.
```
Please develop a React component which will render a div 
after a mouse click. Then, after 1 minute, the div will 
disappear automatically.
```

ChatGPT output: 
Sure! Below is an example of a React component that renders a div after a mouse click and automatically disappears after 1 minute:
```javascript
import React, { useState, useEffect } from 'react';

const AutoHideDiv = () => {
  const [showDiv, setShowDiv] = useState(false);

  useEffect(() => {
    let timer;

    if (showDiv) {
      // Set a timer to hide the div after 1 minute (60000 milliseconds)
      timer = setTimeout(() => {
        setShowDiv(false);
      }, 60000);
    }

    // Clean up the timer when the component unmounts or the showDiv state changes to false
    return () => clearTimeout(timer);
  }, [showDiv]);

  const handleButtonClick = () => {
    setShowDiv(true);
  };

  return (
    <div>
      <button onClick={handleButtonClick}>Click Me</button>
      {showDiv && <div style={{ backgroundColor: 'lightblue', padding: '10px', marginTop: '10px' }}>This div will disappear after 1 minute.</div>}
    </div>
  );
};

export default AutoHideDiv;
```
ChatGPT explanation: 
In this component, we use the useState hook to track the state of whether the div should be visible (showDiv). When the button is clicked, we set showDiv to true, which will cause the div to be rendered.

The useEffect hook is used to set a timer that will automatically hide the div after 1 minute when showDiv is true. If the user clicks the button again before the timer completes, the previous timer will be cleared, and a new one will be set for the new 1-minute interval.

Remember to include this AutoHideDiv component in your main application or another parent component to see it in action.

## Test
Use the following prompt for chatGPT to write a test for the component.
```
Please also develop a unit test for this component?
```

```javascript
import React from 'react';
import { render, fireEvent, waitFor, screen } from '@testing-library/react';
import AutoHideDiv from './AutoHideDiv';

// Mock the setTimeout function
jest.useFakeTimers();

describe('AutoHideDiv', () => {
  it('should render the div after clicking the button and hide it after 1 minute', async () => {
    render(<AutoHideDiv />);

    // Find the button and click it
    const button = screen.getByText('Click Me');
    fireEvent.click(button);

    // The div should be visible after clicking the button
    const div = screen.getByText('This div will disappear after 1 minute.');
    expect(div).toBeVisible();

    // Fast-forward time by 1 minute
    jest.advanceTimersByTime(60000);

    // Wait for the div to be removed
    await waitFor(() => {
      expect(div).not.toBeInTheDocument();
    });
  });

  it('should not render the div initially', () => {
    render(<AutoHideDiv />);

    // The div should not be visible initially
    const div = screen.queryByText('This div will disappear after 1 minute.');
    expect(div).not.toBeInTheDocument();
  });

  it('should hide the div immediately when the button is clicked again before 1 minute', async () => {
    render(<AutoHideDiv />);

    // Find the button and click it
    const button = screen.getByText('Click Me');
    fireEvent.click(button);

    // The div should be visible after clicking the button
    const div = screen.getByText('This div will disappear after 1 minute.');
    expect(div).toBeVisible();

    // Click the button again before 1 minute
    fireEvent.click(button);

    // The div should be hidden immediately
    expect(div).not.toBeInTheDocument();
  });
});
```

In this test, we use render from React Testing Library to render the AutoHideDiv component. We use fireEvent to simulate a click on the button. Then, we use screen queries to check if the div is visible or not. We fast-forward time using jest.advanceTimersByTime to simulate the 1-minute wait. Finally, we use waitFor from React Testing Library to ensure that the div is no longer in the DOM after 1 minute.

By running these tests, you can ensure that the AutoHideDiv component behaves as expected and hides the div after 1 minute automatically.

## Conclusion

ChatGPT can successfully create the component code and test code. 