 var dbPromise = idb.open('rescatado-db', 1, function(upgradeDb) {
  upgradeDb.createObjectStore('rescatado',{keyPath:'pk'});
 });

 fetch('http://127.0.0.1:8000/index/getdata').then(function(response){
  return response.json();
 }).then(function(jsondata){
  dbPromise.then(function(db){
   var tx = db.transaction('rescatado', 'readwrite');
     var feedsStore = tx.objectStore('rescatado');
     for(var key in jsondata){
      if (jsondata.hasOwnProperty(key)) {
        feedsStore.put(jsondata[key]); 
      }
     }
  });
 });