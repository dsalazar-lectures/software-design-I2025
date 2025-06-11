# Proxy Design Pattern

- **Type of Pattern**: Structural.

## Function

The proxy design pattern provides a  **placeholder** object that controls access to another object. It acts as an intermediary, allowing you to perform actions before or after requests reach the original object.

**Advantages**
- Helps dealing with resource-intensive objects, as the original objects is not loaded if not necessary.
- Can manage access to remote resources.
- Can implement access control.
- Adding a layer of security or logging.

The proxy maintains the same interface as the real object, allowing it to be used as one would the real object while adding the functionalities above.

**Disadvantages**

- Adds a new layer of abstraction, thus increasing complexity.
- Can make it slower to load an object if lazy loading is not needed.
- Adds overhead.

## Example: A File Loading Interface

Suppose you are in dire need of a file loading system, and you have limited resources. Main memory is the least of your worries, but you slow CPU and your 2001 rotational hard drive disk that is barely hanging on make a deadly combo for anyone wanting to load a 50kB image in less than half a minute.

So, with this in mind, you look at the *Proxy Design Pattern*, one that would allow you to cache the files in memory through a Proxy object, and would minimize the times you actually need to load the file with your hard-working CPU and the relic you call secondary storage.

*Note: this example, though not a complete solution, provides the necessary structure to help visualize how the Proxy Pattern can be useful.*

## File Structure

- `FileInterface`: A simple abstract interface for loading images. Has one virtual method `display()`.

- `RealFile`: The real file object, has to access disk to load.

- `FileProxy`: The *proxy*. When `RealFile` first loads the file, stores it in cache for future loading.

- `Main`: The main procedure, test the classes above.

## Usage

This example is run in a native Fedora 40 Workstation enviroment, different systems may need to run it slightly different.
### Requirements

- Python3

### Running the program

In a terminal located inside the actual directory [proxy/](.), type:

```bash
python file_loading_interface/main.py
```

### Expected output
```
Proxy Pattern for File Loading Interface
--------------------------------------------------
Using RealFile directly:

RealFile::loadFromDisk(): Loading file from disk...
RealFile::loadFromDisk(): File loaded from disk successfully.
RealFile::display(): Displaying file content...
RealFile::display(): File content: 
            _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(
RealFile::loadFromDisk(): Loading file from disk...
RealFile::loadFromDisk(): File loaded from disk successfully.
RealFile::display(): Displaying file content...
RealFile::display(): File content: 
            _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(

Using FileProxy to manage RealFile:

RealFile::loadFromDisk(): Loading file from disk...
RealFile::loadFromDisk(): File loaded from disk successfully.
RealFile::display(): Displaying file content...
RealFile::display(): File content: 
                  _         _
      __   ___.--'_`.     .'_`--.___   __
     ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
     _\.'_'      _.-'     `-._      `_`./_
    ( \`. )    //\`         '/\\    ( .'/ )
     \_`-'`---'\\__,       ,__//`---'`-'_/
      \`        `-\         /-'        '/
       `                               '     
    
FileProxy::display(): File content already loaded. Displaying cached content...
Cached content: 
                  _         _
      __   ___.--'_`.     .'_`--.___   __
     ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
     _\.'_'      _.-'     `-._      `_`./_
    ( \`. )    //\`         '/\\    ( .'/ )
     \_`-'`---'\\__,       ,__//`---'`-'_/
      \`        `-\         /-'        '/
       `                               '     
    
```

### How to interpret the output?

The example shows two ways of loading a file; one directly with the `RealFile`, and one using `FileProxy`. Each simulated load from disk last 3 seconds, and both files are loaded 2 times.

The `RealFile` file is loaded twice from disk, and lasts 6 seconds to load both.

The `ProxyFile` on the other hand, only loads the file one time from disk, and it lasts 3 seconds to load both, as the second time the file is already cached in main memory.

## Credits

Gabriel Serrano Rojas, 2025. <gabriel.serranorojas@ucr.ac.cr>

## Used material

- Refactoring Guru @ https://refactoring.guru/design-patterns/proxy.
- GeeksforGeeks @ https://www.geeksforgeeks.org/proxy-design-pattern/.
