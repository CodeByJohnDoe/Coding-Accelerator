
 # Time : 2 h

class Say_My_Name
    attr_reader     :path_abs

    # Catch Path
    def catch_path
        @path_abs = File.expand_path(__FILE__)
    end

    # Send Name
    def send_name
        puts File.basename(path_abs)
    end    
end

if __FILE__ == $0 
    smn = Say_My_Name.new

    smn.catch_path
    smn.send_name

end