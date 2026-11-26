# A catalogue witness

[The example soul](soul.yaml) follows a contested archive entry. Its primary value of accountability puts a contributor’s withdrawal procedure ahead of search reach. Its mutualist pack adds a question about who can change that procedure.

From the repository root:

```sh
python scripts/validate_soul.py --resolve examples/minimal_soul/soul.yaml
python scripts/negative_criterion.py examples/minimal_soul/soul.yaml
python scripts/soul_to_prompt.py examples/minimal_soul/soul.yaml
```

Look for the declared withdrawal condition, the witness role and the mutualist questions in the prompt. Validation checks their format and resolution. Try a revised soul with an unfamiliar pack name to see what a broken reference looks like.
