def format_log(query, response):
    from datetime import datetime
    return {
        "query": query,
        "response": response,
        "timestamp": datetime.now()
    }
