# github-demo

Demos for Bugout GitHub integration.


## Bugout on GitHub

Bugout is a knowledge management system for software teams.

### Add checklists to your pull requests

Use Bugout to create a checklist of steps that must be taken before a change can be deployed. This checklist can include things like running database migrations, setting environment variables, or modifying a load balancer.

![Screenshot of check require](img/ci-example-1.png)

Just mention `@bugout-dev` when you want to cross items off this checklist:

```
@bugout-dev check accept "Run alembic migration"
```

View the current status of your checklist on the `@bugout-dev` details page:

![Check Detail status](img/ci-example-2.png)

> TRY THIS on our [demo PR](https://github.com/bugout-dev/github-demo/pull/2)!

### Easier code reviews

[**Locust**](https://github.com/bugout-dev/locust) is a static analyzer that summarizes pull requests.

You can also use a JSON representation of Locust metadata in your CI/CD environments to program checks like: "Every time we add a function, we should add a test in the corresponding testing module."

![Screenshot of Locust summary](img/locust-example-1.png)


## Using Bugout

### Installation

- Visit [Bugout GitHub Bot](https://github.com/apps/bugout-dev)

- Install it in an organization or on individual repositories

### Set up continuous integration

- Go to settings of current repository

- Chose `Branches` and `Add rule` in section `Branch protection rules`

![Branch protection rules](img/check-setup-1.png)

- Add rule `Require status checks to pass before merging`

![Check branch rule](img/check-setup-2.png)

**At this point, you have access to Bugout Checklists**

### Work with Bugout Checklists!

- To add a new check, create a comment on your Pull Request:
```
@bugout-dev check require <your crucial check>
```

- To accept  check:
```
@bugout-dev check accept <your crucial check>
```

- View the details of the `@bugout-dev` job to see the status of your checklist.

> **Note:** You can put your phrase in quotes or without it

To be unlock Locust summaries and run static analysis, you will need a Bugout account and will have to set up a GitHub Action.

### Register at Bugout and generate token

- Visit [Bugout](https://bugout.dev) website and create account

- Generate new token at [Bugout Tokens](https://bugout.dev/account)

![Add new token](img/token-add-1.png)

### Add token to GitHub Secrets

- Add generated token to Organization `Secrets` and call it as `BUGOUT_SECRET`

![Bugout secret at GitHub](img/secret-setup-1.png)

### Prepare Locust

- Add file `locust.yaml` in `.github/workflow/` repository. Copy the template [here](https://github.com/bugout-dev/github-demo/blob/main/.github/workflows/locust.yaml)
- Be sure this file exists in `main` or `master` branch and your new Pull Request branches include `.github/workflow/locust.yaml`.

### Generate your first Locust summary!

- Create new Pull Request, please see our [example PR](https://github.com/bugout-dev/github-demo/pull/2)
- Wait a bit until GitHub Action `Locust` completes
- And just type a comment:
```
@bugout-dev summarize
```

## Resources & Links


- [Bugout website](https://bugout.dev)

- [Bugout GitHub Bot](https://github.com/apps/bugout-dev)

- [Bugout Locust package](https://github.com/bugout-dev/locust)

- [`locust.yaml` starter](https://github.com/bugout-dev/github-demo/blob/main/.github/workflows/locust.yaml)
