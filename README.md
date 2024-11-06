# Kenny's Testing Step Generate

This is a CLI that should generate testing steps.

## Installation

Simply run `pip install testing-step-generator`. This was designed using `Python 3.11`,
so you should probably have that installed.

## Commands

### init

You need to run this `init` command, using `tsg init` before you do anything.
This will prompt you to enter your OpenAi API key, which you can get once you
make an OpenAi develop account. Follow their [guide](https://platform.openai.com/docs/quickstart)

This will save the API key in the `.tsg` directory in your root.

### generate

Run using `tsg generate` from the branch of your project you want to get testing steps for.
By default this will comapre it against the `master` branch. However, you can specify a branch
with `-b` or `--branch`, e.g., `tsg generate --branch other_branch`
