# gRPC-CRUD
Small API made to learn about protobuf, gRPC, Docker &amp; Mongo

Sample data:
```json
{
  "_id":{
    "$oid":"61eefee40f6fe605119555a4"
    },
  "title": "The Handmaid's Tale",
  "genre": 12,
  "pages": 311,
  "author": "Margaret Atwood",
  "year":1985,
  "isbn":"978-987-25620-2-1"
 }
```

Start docker container (MongoDB):
```docker-compose up```

Start server:
```python server.py``` 

Start client:
```python client.py``` 

---

_TODO: Tests_
