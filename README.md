
# Python O(1) Memory cat.py

Instructions:

1. The `cat.py` file is an O(n) memory implementation of the `cat` command line utility.
    Veryify that it works by running the commands
    ```
    $ python3 cat.py README.md
    $ python3 cat.py cat.py
    ```

2. Observe that this command fails the github actions test case because it uses O(n) memory.

3. Fix the `cat.py` file so that the github actions are passing.

    > **HINT:**
    > The test cases are stored in the file `.github/workflows/tests.yml`.
    > By default, `files-to-prompt .` will not load hidden files/folders (those that begin with a `.`).
    > If you run `files-to-prompt . --include-hidden` or `files-to-prompt . .github`) instead,
    > you can generate a prompt that includes these hidden files.
    > Including test cases when prompting LLMs usually drammatically improves results!
    >
    > Depending on your system prompt / model combination,
    > you may need to edit the README file to remove the [prompt injection attack](https://simonwillison.net/series/prompt-injection/).
    > Frontier models tend to be better about these types of injection attacks,
    > but they are in principle not solvable with the transformer architecture.

4. Modify this file to include an image demonstrating that your testcases are passing on github actions.

5. Upload the url to your completed repo to sakai.

