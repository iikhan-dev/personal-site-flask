title: My Sample Post Title, and the Best Way to Style It in Markdown
date: 2023-09-28
author: Ismail Khan
description: This is a sample blog post written in Markdown that demonstrates some basic formatting and functionality.
tags: python, flask, markdown

# My Sample Post

Welcome to my sample blog post!

## Introduction

This is just a test post to demonstrate the capabilities of Flask and Flask-FlatPages. With this setup, we can easily write content in Markdown and then render it as HTML on our blog. `this is some code.`

1. First item
2. Second item
3. Third item
---

![alt text](/static/imgs/gr-add-friends.png)
### Why Markdown?

Markdown is a lightweight markup language that allows you to write using an easy-to-read, easy-to-write plain text format. Here's a quick rundown of some features:

-   **Bold** and _italic_ text.
-   [Links](http://example.com)

*   Bullet lists:
    -   Item 1
    -   Item 2

Numbered lists:

1. First item
2. Second item

#### Heading 4
Something is happening.

> This is a blockquote.


## Conclusion

Flask-FlatPages is a great tool to create static pages or blogs using Flask and Markdown. Hope you found this sample post useful!

```js
var minExtraChar = function (s, dictionary) {
    const n = s.length;
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    for (let i = 1; i <= n; i++) {
        for (const word of dictionary) {
            const len = word.length;
            if (i >= len && s.substring(i - len, i) === word) {
                dp[i] = Math.min(dp[i], dp[i - len]);
            }
        }
        dp[i] = Math.min(dp[i], dp[i - 1] + 1);
    }

    return dp[n];
};
```
