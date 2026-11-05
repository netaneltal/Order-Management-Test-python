products = [
            {"id": 1, "name": "Keyboard", "price": 120},
            {"id": 2, "name": "Mouse", "price": 80},
            {"id": 3, "name": "Monitor", "price": 900},
            {"id": 4, "name": "Headphones", "price": 200},
            {"id": 5, "name": "USB Cable","price": 30}
           ]
orders = [{
          "id": 1,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "OPEN"
          },{
          "id": 2,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "closs"
          }]
order =   {
          "id": 1,
          "items": [{"product_id": 1, "quantity": 2},
                     {"product_id": 3, "quantity": 1}],
          "total": 1026.0,
          "status": "OPEN"
          }