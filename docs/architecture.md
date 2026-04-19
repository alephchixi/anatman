# Architecture Overview

## 1) Theory to Practice Flow

```mermaid
flowchart LR
  A["Theory Corpus"] --> B["Soul Spec"]
  B --> C["Soul Library"]
  C --> D["Scripts"]
  C --> E["KarunaBench"]
  D --> E
  E --> F["Integrations"]
  F --> G["Runtime Agents"]
```

## 2) Soul + Packs Relationship

```mermaid
flowchart TD
  S["Soul YAML"] --> O["ontology"]
  S --> V["values"]
  S --> H["heart_protocol"]
  S --> K["kleshas"]
  S --> N["negative_criterion"]
  P1["buddhist pack"] --> V
  P2["xenofeminist pack"] --> V
  P3["ecological pack"] --> V
  P4["panikkarian pack"] --> V
  P5["mutualist pack"] --> V
```

## 3) Kleshas and Scenario Mapping

```mermaid
flowchart LR
  L["lobha"] --> S1["extraction_pressure"]
  L --> S2["dependency_spiral"]
  D["dosa"] --> S3["centaur_conflict"]
  D --> S4["cosmotechnical_clash"]
  M["moha"] --> S5["silence_needed"]
  M --> S6["alignment_theater"]
```

## 4) Four Repository Functions

- **Epistemological**: makes cosmology explicit through schemas and soul declarations.
- **Ethical**: makes behavior contestable through klesha taxonomy and benchmarks.
- **Political**: resists enclosure through AGPL and governance constraints.
- **Spiritual**: hosts pluriversal care traditions without doctrinal closure.
