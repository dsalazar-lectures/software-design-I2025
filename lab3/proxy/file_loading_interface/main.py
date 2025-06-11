if __name__ == "__main__":
    from FileInterface import FileInterface
    from RealFile import RealFile
    from FileProxy import FileProxy

    print("Proxy Pattern for File Loading Interface")
    print("--------------------------------------------------")
    print("Using RealFile directly:\n")
    file0: FileInterface = RealFile(
        r"""
            _   _
           (.)_(.)
        _ (   _   ) _
       / \/`-----'\/ \
     __\ ( (     ) ) /__
     )   /\ \._./ /\   (
      )_/ /|\   /|\ \_(""")
    file0.display()  # Directly using the real file without proxy
    file0.display()  # Displaying again to show that it loads each time
    print("\nUsing FileProxy to manage RealFile:\n")
    # Create a real file object
    file1: FileInterface = RealFile(
        r"""
                  _         _
      __   ___.--'_`.     .'_`--.___   __
     ( _`.'. -   'o` )   ( 'o`   - .`.'_ )
     _\.'_'      _.-'     `-._      `_`./_
    ( \`. )    //\`         '/\\    ( .'/ )
     \_`-'`---'\\__,       ,__//`---'`-'_/
      \`        `-\         /-'        '/
       `                               '     
    """)
    # Create a proxy for the real file
    file1_proxy: FileInterface = FileProxy(file1)
    # Display the file content using the proxy
    file1_proxy.display()
    # Display the file content again to demonstrate caching
    file1_proxy.display()

