# FastAPI and Pydantic Examples

A collection of practical examples demonstrating how to use Pydantic for data validation and how to integrate those patterns into FastAPI applications. This repository contains standalone Pydantic example scripts and notes for learning Pydantic v2 features, plus guidance for using Pydantic models inside FastAPI endpoints.

## Overview

This repository contains learning examples showcasing essential Pydantic concepts, from basic field validation to advanced features like computed fields and model validators. Many of these patterns are commonly used when building APIs with FastAPI, which relies on Pydantic for request/response validation.

## Examples Included

### 1. `pydantic1.py` - Field Validators
Demonstrates basic field-level validation:
- Type validation (str, float, int)
- Field constraints using `Field()` with validation rules (`gt`, `lt`)
- Email validation using `EmailStr`
- URL validation using `AnyUrl`
- Custom field validators with `@field_validator`
- Email domain validation (whitelist approach)
- Field transformation (converting names to uppercase)

**Key Concepts:** `Field()` for constraint metadata, `@field_validator` decorators with `mode='before'` and `mode='after'`, Email and URL type validation

### 2. `pydantic3.py` - Model Validators
Demonstrates cross-field validation and model-level logic:
- Complex types: `Optional`, `List`, `Dict`
- Model-level validation using `@model_validator`
- Cross-field validation rules (e.g., emergency contact required for age > 60)
- Data relationships and business logic

**Key Concepts:** `@model_validator(mode='after')` for validating entire model after parsing, multi-field validation logic, optional fields

### 3. `pydantic4_computedfield.py` - Computed Fields
Demonstrates automatic derived fields:
- Computed fields using `@computed_field` and `@property`
- Deriving values from other fields (BMI calculation)
- Fields not provided by users but calculated on-the-fly

**Key Concepts:** `@computed_field` decorator, derived data without user input, mathematical computations on model data

### 4. `pydntic.py` - Advanced Field Annotations
Demonstrates advanced field documentation and metadata:
- `Annotated` types for complex field metadata
- Field constraints: `max_length`, `title`, `description`
- Field examples for documentation
- Optional fields with defaults
- Complex nested types: `Optional[List[str]]`, `Dict[str, str]`

**Key Concepts:** `Annotated[Type, Field(...)]` for rich metadata, field documentation and examples, JSON schema generation from fields

## FastAPI Integration

These Pydantic examples are directly applicable inside FastAPI apps. Typical usage patterns:

- Use Pydantic models as request bodies and response models in FastAPI endpoints.
- Leverage field validation and model validators to enforce business rules on incoming requests.
- Use computed fields / properties for derived response values.

To add a simple FastAPI example, create a file (for example `app.py`) with:

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

app = FastAPI()

@app.post('/patients', response_model=Patient)
def create_patient(patient: Patient):
    return patient
```

Run with:

```bash
uvicorn app:app --reload
```

## Getting Started

### Prerequisites

This repository is Python-only (100% Python). To run the examples and any FastAPI apps you add, install the required packages:

```bash
pip install pydantic fastapi uvicorn
```

If you only want to run the standalone Pydantic scripts, `pydantic` alone is sufficient:

```bash
pip install pydantic
```

### Running Examples

Each Pydantic example file can be run independently:

```bash
python pydantic1.py
python pydantic3.py
python pydantic4_computedfield.py
python pydntic.py
```

If you add a FastAPI app file (for example `app.py`), run it using uvicorn as shown above.

### Example Output (from the example scripts)

```
SANA
20
abc@hdfc.com
inserted
```

## Key Pydantic Features Demonstrated

- Type Validation — `pydantic1.py`: Ensure data types match schema
- Field Constraints — `pydantic1.py`: Validate ranges, lengths, formats
- Custom Validators — `pydantic1.py`: Domain-specific business logic
- Email/URL Types — `pydantic1.py`: Built-in validation for common types
- Model Validators — `pydantic3.py`: Cross-field relationships & logic
- Computed Fields — `pydantic4_computedfield.py`: Derived/calculated values
- Field Metadata — `pydntic.py`: Documentation & schema generation
- Optional & Nested Types — `pydantic3.py`, `pydntic.py`

## Use Cases

- API Development: Validate request/response data in FastAPI, Flask, or Django applications
- Data Pipelines: Ensure data quality before processing
- Configuration Management: Validate and parse config files
- Database Models: Define schemas with automatic validation
- CLI Applications: Parse and validate command-line arguments

## Learning Resources

- Official Pydantic Documentation: https://docs.pydantic.dev/
- Pydantic GitHub Repository: https://github.com/pydantic/pydantic
- Pydantic v2 Migration Guide: https://docs.pydantic.dev/latest/concepts/models/

## Notes

- File `pydntic.py` contains a typo in the filename (missing 'a' in pydantic). This is intentional in the examples.
- The repository language composition is Python (100%).

Created for learning Pydantic v2 features and demonstrating common FastAPI integration patterns.
