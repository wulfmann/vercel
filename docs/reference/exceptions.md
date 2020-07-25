# Exceptions

## VercelError

If an API request returns an `error` block in the response, a  `VercelError` exception is thrown. It exposes the following properties:

|Name|Description|
|----|----|
|code|The value from the `code` field on the response|
|message|The value from the `message` field on the response|

## UnknownError

If an exception is thrown during the API request, but there is no `error` block in the response, a `UnknownError` exception is thrown.
