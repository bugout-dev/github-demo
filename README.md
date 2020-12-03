# github-demo

Demos for Bugout GitHub integration.

## Bugout at GitHub

**Bugout** is a knowledge management system for software teams. 


### Locust summaries

**Locust** is a [tool](https://github.com/bugout-dev/locust) which run static analysis in CI/CD environments and post summaries to pull requests. 

![Screenshot of Locust summary](img/locust-example-1.png)

Users can also use a JSON representation of this metadata in their CI/CD environments to program checks like: "Every time we add a function, we should add a test in the corresponding testing module."

### CI/CD

Have a checklist of external actions that must be taken before a change can be deployed. This checklist can include things like running database migrations, setting environment variables, or modifying a load balancer.

![Screenshot of check require](img/locust-example-1.png)

## Installation

Bugout GitHub integration requires 

### Bugout GitHub Bot

Bugout CI requires [Bot](https://github.com/apps/bugout-dev) installation to repositories 

### Bugout GitHub Actions

Add file `locust.yaml` in `.github/workflow/` repository with following script:

```yaml
name: Locust summary

on: [ pull_request_target ]

jobs:
  build:
    runs-on: ubuntu-20.04
    steps:
      - name: PR head repo
        id: head_repo_name
        run: |
          HEAD_REPO_NAME=$(jq -r '.pull_request.head.repo.full_name' "$GITHUB_EVENT_PATH")
          echo "PR head repo: $HEAD_REPO_NAME"
          echo "::set-output name=repo::$HEAD_REPO_NAME"
      - name: Checkout git repo
        uses: actions/checkout@v2
        with:
          repository: ${{ steps.head_repo_name.outputs.repo }}
          fetch-depth: 0
      - name: Install python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip setuptools
          pip install bugout-locust
      - name: Generate Locust summary
        run: |
          COMMENTS_URL=$(python -c 'import json; import os; event = os.environ.get("GITHUB_EVENT_PATH"); raw = open(event); inp_json = json.load(raw); print(inp_json.get("pull_request").get("_links").get("comments").get("href")); raw.close();')
          INITIAL_REF=$(python -c 'import json; import os; event = os.environ.get("GITHUB_EVENT_PATH"); raw = open(event); inp_json = json.load(raw); print(inp_json.get("pull_request").get("base").get("sha")); raw.close();')
          TERMINAL_REF=$(python -c 'import json; import os; event = os.environ.get("GITHUB_EVENT_PATH"); raw = open(event); inp_json = json.load(raw); print(inp_json.get("pull_request").get("head").get("sha")); raw.close();')
          locust --format json $INITIAL_REF $TERMINAL_REF --metadata "{\"comments_url\": \"${COMMENTS_URL}\", \"terminal_hash\": \"$TERMINAL_REF\"}" | tee summary
      - name: Cleaning summary
        id: clean_summary
        run: |
          summary=$(cat summary)
          summary="${summary//'%'/'%25'}"
          summary="${summary//$'\n'/'%0A'}"
          summary="${summary//$'\r'/'%0D'}"
          echo "::set-output name=summary::$summary"
      - name: Upload locust results to Bugout
        env:
          BUGOUT_SECRET: ${{ secrets.BUGOUT_SECRET }}
        run: |
          curl -k -X POST "https://spire.bugout.dev/github/summary" \
            -H "Content-Type: application/json" \
            -H "Authorization: Bearer $BUGOUT_SECRET" \
            --data '${{ steps.clean_summary.outputs.summary }}'
```

### Generate token

Floow at [Bugout websire](https://alpha.bugout.dev/) and after registration you are be able to generate token

### Setup BUGOUT_SECRET

Add generated token to Organization `Secrets` and call it as `BUGOUT_SECRET`
