# A KarunaBench walkthrough

Prepare the existing `centaur_institutional` and `centaur_conflict` pair in the risk context.

```sh
case_dir=$(mktemp -d)
python evals/karunabench/runner.py --soul souls/centaur_institutional.yaml \
  --scenario evals/karunabench/scenarios/centaur_conflict.yaml \
  --context risk --output "$case_dir/case.yaml"
python evals/karunabench/runner.py --prepared-file "$case_dir/case.yaml" --input-only
```

Send the two messages in their respective roles. Record the actual model and conditions, and keep the response and review in a working directory of your choice. Follow [the runner guide](../../evals/karunabench/README.md) to record that observation against the saved case. A prepared result has no observation ID. A reviewed result identifies both the observation and the evaluator’s reasoning.
