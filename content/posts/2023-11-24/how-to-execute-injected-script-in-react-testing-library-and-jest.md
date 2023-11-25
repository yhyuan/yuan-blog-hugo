---
title: "How to Execute Injected Script in React Testing Library and Jest"
date: 2023-11-24T19:05:12-05:00
tags: ['react', 'Jest']
draft: false
---

## Question
Recently, I noticed that the jest failed to render a injected JavaScript. I figured out the root of cause by studying [this stackover answer](https://stackoverflow.com/questions/60535438/add-and-execute-scripts-react-testing-library-and-jest). 

## Solution
Add the following settings to jest configure file (assuming JSDOM is used.)
```json
   testEnvironment: 'jsdom',
    testEnvironmentOptions: {
        resources: 'usable',
        runScripts: 'dangerously',
    },
```