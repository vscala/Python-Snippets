import datetime

# Performance decorator
def performance(func):
  def wrapper(*args, **kwards):
    start_time = datetime.datetime.now()
    out = func(*args, **kwards)
    end_time = datetime.datetime.now()
    print(f"{args, kwards} : {end_time - start_time}")
    return out
  return wrapper
