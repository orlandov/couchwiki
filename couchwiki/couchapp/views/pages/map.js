function(doc) {
    if (doc.type && doc.type == "page") {
        var url_name = doc._id.replace(/^page_/, '');
        emit(doc._id, { name: doc.name, url_name: url_name });
    }
}
