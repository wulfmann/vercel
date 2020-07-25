# Pagination

All resources that have a `list` operation will return an object with a `iter` method.

The `iter` method returns an iterator that handles the [pagination] block in the API response.

Example:

```python
projects = vercel.Project.list()

for project in projects.iter():
  print(project.id) # pro_xxx
```

