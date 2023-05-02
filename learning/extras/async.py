import asyncio # for asynchronous functions

async def my_async_function():
    print("Starting...")
    await asyncio.sleep(1) # thanks to this we can let this function rest while the rest of the code execute, for example.
    print("...Finished!")

async def main(): # defining main (functions that run other func)
    await my_async_function() # calls and await func until it's done

asyncio.run(main())  # obligatory, runs main and when done terminates the program

# The main() function calls an async function called my_async_function() using the await keyword. This means that my_async_function() is an asynchronous function that will run concurrently with other code.

# Finally, the asyncio.run() function is used to run the main() function in an event loop. This function is part of the asyncio module in Python and it allows you to run asynchronous code in a synchronous way. When the main() function completes, the event loop will exit and the program will terminate.