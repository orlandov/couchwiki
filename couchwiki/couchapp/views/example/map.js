function(doc) {
  var k, keys = []
  for (k in doc) keys.push(k);
  emit(doc._id, keys);
};
