# GitHub Actions Context and Environment Variables

| Context/Environment Variable | Description                                                              | Example                                               |
| ---------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- |
| **`github`**                 | Overall context for GitHub-provided information.                         | -                                                     |
| `github.event_name`          | The name of the event that triggered the workflow.                       | `push`, `pull_request`, `schedule`                    |
| `github.ref`                 | The branch or tag ref that triggered the workflow.                       | `refs/heads/main`                                     |
| `github.ref_name`            | The short name of the ref (branch or tag) that triggered the workflow.   | `main`                                                |
| `github.sha`                 | The commit SHA that triggered the workflow.                              | `d6fde92930d4715a2b49857d24b940956b26e4c2`            |
| `github.actor`               | The name of the person or app that initiated the workflow run.           | `octocat`                                             |
| `github.repository`          | The name of the repository (owner/repo).                                 | `octocat/hello-world`                                 |
| `github.repository_owner`    | The owner of the repository.                                             | `octocat`                                             |
| `github.run_id`              | The unique identifier (ID) of the workflow run.                          | `1658821493`                                          |
| `github.run_number`          | The unique number for each run of a particular workflow in a repository. | `42`                                                  |
| `github.job`                 | The ID of the current job.                                               | `build`                                               |
| `github.workflow`            | The name of the workflow.                                                | `CI`                                                  |
| `github.action`              | The name of the action.                                                  | `actions/checkout@v2`                                 |
| `github.event_path`          | The path to the file with the complete webhook event payload.            | `/home/runner/work/_temp/_github_workflow/event.json` |
| `github.workspace`           | The path to the GitHub workspace directory.                              | `/home/runner/work/my-repo-name/my-repo-name`         |
| `github.token`               | A token to authenticate on behalf of GitHub Actions.                     | `***` (masked)                                        |
| `github.action_path`         | The path where an action is located.                                     | `/home/runner/work/_actions/my-action`                |
| `github.action_ref`          | The ref for the action's repository.                                     | `v2`                                                  |
| `github.head_ref`            | The head branch of the pull request.                                     | `feature-branch`                                      |
| `github.base_ref`            | The base branch of the pull request.                                     | `main`                                                |
| `github.server_url`          | The URL of the GitHub server.                                            | `https://github.com`                                  |
| `github.api_url`             | The URL of the GitHub API.                                               | `https://api.github.com`                              |
| `github.graphql_url`         | The URL of the GitHub GraphQL API.                                       | `https://api.github.com/graphql`                      |
| **`env`**                    | Environment variables set for the job.                                   | -                                                     |
| `env.MY_VAR`                 | Custom environment variable set in the workflow.                         | `Hello, World!`                                       |
| **`jobs`**                   | Information about all jobs in the workflow.                              | -                                                     |
| `jobs.<job_id>.status`       | The status of a job (`success`, `failure`, `cancelled`).                 | `success`                                             |
| `jobs.<job_id>.outputs`      | Outputs from a previous job.                                             | -                                                     |
| **`job`**                    | Information about the current                                            |                                                       |
| `job.status`                 | The status of the current job (success, failure).                        |                                                       |
| `job.outputs`                | Outputs from the current job.                                            |                                                       |
| **`steps`**                  | Context about individual steps within a job.                             |                                                       |
| `steps.<step_id>.outputs`    | Outputs from a specific step.                                            |                                                       |
| **`runner`**                 | Information about the runner executing the job.                          |                                                       |
| `runner.os`                  | The operating system of the runner.                                      | `Linux`                                               |
| `runner.arch`                | The architecture of the runner.                                          | `x64 `                                                |
| `runner.name`                | The name of the runner executing the job.                                | `Hosted Agent`                                        |
| `runner.temp`                | The directory for temporary files.                                       | `/home/runner/work/\_temp`                            |
| `runner.tool_cache `         | The directory containing preinstalled tools.                             | `/opt/hostedtoolcache `                               |
| **`matrix`**                 | Information about the matrix of values in the workflow.                  |                                                       |
| `matrix.environment `        | The current matrix environment value.                                    | `test`                                                |
| **`needs`**                  | Context from previous jobs that are required.                            |                                                       |
| `needs.<job_id>.outputs`     | Outputs from a job that this job needs.                                  |                                                       |
| **`inputs`**                 | Inputs provided to the workflow.                                         |                                                       |
| `inputs.<input_name>`        | Value of the input provided.                                             |                                                       |
| **`strategy`**               | Strategy settings for the job.                                           |                                                       |
| `strategy.fail-fast`         | Whether to fail the job fast on a failure.                               | `true`                                                |
| **`secrets`**                | Secret variables set in GitHub.                                          |                                                       |
| `secrets.MY_SECRET`          | Secret set in GitHub Secrets.                                            | `my_secret_value`                                     |
| **`vars`**                   | Variables defined in the workflow.                                       |                                                       |
| `vars.<var_name>`            | Value of a defined variable.                                             |                                                       |
| **`about`**                  | General information about the workflow.                                  |                                                       |
| `about.version`              | The version of the workflow schema.                                      | `1.0.0`                                               |
