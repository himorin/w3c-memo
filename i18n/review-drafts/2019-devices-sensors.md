# Devices and Sensors Reviews, 4 docs

- [tracker](https://github.com/w3c/i18n-activity/issues/780)
  - WebDriver API and its extensions enable test automation and are not web-exposed in a normal browsing scenario. The extensions in scope of this review request are defined in the following Automation sections
- [Generic Sensor](https://w3c.github.io/sensors/#automation)
- [Accelerometer](https://w3c.github.io/accelerometer/#automation)
- [Gyroscope](https://w3c.github.io/gyroscope/#automation)
- [Orientation sensor](https://w3c.github.io/orientation-sensor/#automation)

# memo

## Generic sensor

- No handling of natural language or user input
- This defines framework, mock sensors does not define return value syntax (nor unit), data formats are defined by each sensor specification
  - and each specification only defines its specific data format
- time related values are in Hz or DOMHighResTimeStamp, no dependency to TZ or cultural text

## Accelerometer

- Just a definition of data dictionaly
- Defines one dictionary (and two extensions) which has values with well defined SI unit

## Gyroscope

- Just a definition of data dictionaly
- Defines one dictionary which has values with well defined SI unit

## Orientation sensor

- Just a definition of data dictionaly
- Defines one dictionary (and one extention) which has quaternion of rotation matrix (normalized)

