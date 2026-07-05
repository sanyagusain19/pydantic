# Pydantic Learning Examples

A collection of practical examples demonstrating core features of **Pydantic**, the popular Python data validation and parsing library.

## Overview

This repository contains learning examples showcasing essential Pydantic concepts, from basic field validation to advanced features like computed fields and model validators. Each example uses a `Patient` data model to illustrate different validation techniques.

## Examples Included

### 1. **pydantic1.py** - Field Validators
Demonstrates basic field-level validation:
- Type validation (str, float, int)
- Field constraints using `Field()` with validation rules (`gt`, `lt`)
- Email validation using `EmailStr`
- URL validation using `AnyUrl`
- Custom field validators with `@field_validator`
- Email domain validation (whitelist approach)
- Field transformation (converting names to uppercase)

**Key Concepts:**
- `Field()` for constraint metadata
- `@field_validator` decorators with `mode='before'` and `mode='after'`
- Email and URL type validation

### 2. **pydantic3.py** - Model Validators
Demonstrates cross-field validation and model-level logic:
- Complex types: `Optional`, `List`, `Dict`
- Model-level validation using `@model_validator`
- Cross-field validation rules (e.g., emergency contact required for age > 60)
- Data relationships and business logic

**Key Concepts:**
- `@model_validator(mode='after')` for validating entire model after parsing
- Multi-field validation logic
- Optional fields

### 3. **pydantic4_computedfield.py** - Computed Fields
Demonstrates automatic derived fields:
- Computed fields using `@computed_field` and `@property`
- Deriving values from other fields (BMI calculation)
- Fields not provided by users but calculated on-the-fly

**Key Concepts:**
- `@computed_field` decorator
- Derived data without user input
- Mathematical computations on model data

### 4. **pydntic.py** - Advanced Field Annotations
Demonstrates advanced field documentation and metadata:
- `Annotated` types for complex field metadata
- Field constraints: `max_length`, `title`, `description`
- Field examples for documentation
- Optional fields with defaults
- Complex nested types: `Optional[List[str]]`, `Dict[str, str]`

**Key Concepts:**
- `Annotated[Type, Field(...)]` for rich metadata
- Field documentation and examples
- JSON schema generation from fields

## Getting Started

### Prerequisites
```bash
pip install pydantic
```

### Running Examples

Each file can be run independently:

```bash
# Run any example
python pydantic1.py
python pydantic3.py
python pydantic4_computedfield.py
python pydntic.py
```

### Example Output
```
SANA
20
abc@hdfc.com
inserted
```

## Key Pydantic Features Demonstrated

| Feature | Example File | Use Case |
|---------|--------------|----------|
| Type Validation | `pydantic1.py` | Ensure data types match schema |
| Field Constraints | `pydantic1.py` | Validate ranges, lengths, formats |
| Custom Validators | `pydantic1.py` | Domain-specific business logic |
| Email/URL Types | `pydantic1.py` | Built-in validation for common types |
| Model Validators | `pydantic3.py` | Cross-field relationships & logic |
| Computed Fields | `pydantic4_computedfield.py` | Derived/calculated values |
| Field Metadata | `pydntic.py` | Documentation & schema generation |
| Optional Types | `pydantic3.py`, `pydntic.py` | Handle nullable fields |
| Nested Types | `pydantic3.py` | Complex data structures |

## Use Cases for Pydantic

- **API Development**: Validate request/response data in FastAPI, Flask, or Django applications
- **Data Pipelines**: Ensure data quality before processing
- **Configuration Management**: Validate and parse config files
- **Database Models**: Define schemas with automatic validation
- **CLI Applications**: Parse and validate command-line arguments

## Learning Resources

- [Official Pydantic Documentation](https://docs.pydantic.dev/)
- [Pydantic GitHub Repository](https://github.com/pydantic/pydantic)
- [Pydantic v2 Migration Guide](https://docs.pydantic.dev/latest/concepts/models/)

## Common Patterns Used in Examples

### Pattern 1: Dictionary Unpacking
```python
patient_info = {'name': 'sana', 'age': 20, ...}
patient1 = Patient(**patient_info)  # Unpacking with **
```

### Pattern 2: Validation After Model Creation
```python
@model_validator(mode='after')
def validate_model(self):
    # Access all fields after parsing
    return self
```

### Pattern 3: Field Transformation
```python
@field_validator('name')
@classmethod
def name_validator(cls, value):
    return value.upper()  # Transform input
```

## Next Steps

1. Run each example to understand different validation approaches
2. Modify the `Patient` model with your own fields and validation rules
3. Combine techniques from multiple examples for real-world scenarios
4. Explore Pydantic's JSON schema generation: `Patient.model_json_schema()`
5. Integrate with a web framework (FastAPI, etc.) for practical applications

---

**Note:** File `pydntic.py` contains a typo in the filename (missing 'a' in pydantic). This is intentional in the examples.

Created for learning Pydantic v2 features and best practices.
