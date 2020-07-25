# Projects

## Operations

### Get a Project

```python
vercel.Project.get(
  name='my-project'
)
```

### Create a Project

```python
vercel.Project.create(
  name='my-project'
)
```

### Update a Project

```python
project = vercel.Project.create(
  name='my-project'
)

project.update(
  name='new-project'
)
```

### Delete a Project

```python
project = vercel.Project.create(
  name='my-project'
)

project.delete()
```

### Get Environment Variables

```python
project = vercel.Project.create(
  name='my-project'
)

project.get_environment_variables()
```

### Create an Environment Variable

```python
project = vercel.Project.create('my-project')

project.create_environment_variable(
  key='',
  value='',
  target='production'
)
```

### Add a Domain

```python
domain = vercel.Domain.get('test.com')

project = vercel.Project.create(
  name='my-project'
)

project.add_domain(
  domain=domain.id
)
```

### Redirect a Domain

```python
domain = vercel.Domain.get('test.com')

project = vercel.Project.create(
  name='my-project'
)

project.redirect_domain(
  domain='www.test.com',
  redirect=domain.id
)
```

### Remove a Domain

```python
domain = vercel.Domain.get('test.com')

project = vercel.Project.create(
  name='my-project'
)

project.remove_domain(
  domain=domain.id
)
```
