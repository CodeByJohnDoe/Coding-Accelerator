
 # Time : 1 h

 class Carver
    attr_accessor   :arguments

    # Catch Arguments
    def catch_arguments
        @arguments = ARGV
    end

    # Send argument
    def send_argument
        @arguments.respond_to?("each")
        @arguments.each do |item|
            puts "#{item}"                   # .chomp one line
        end
    end    
end

if __FILE__ == $0 
    c = Carver.new

    c.catch_arguments
    c.send_argument

end
