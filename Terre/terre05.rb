
 # Time :  2 h 

 class Peer
    attr_accessor   :argument
        
    def compare

        @argument = ARGV[0].to_i

        if ((@argument.is_a? Integer) && !(ARGV.is_a? String))
            
        @argument = @argument.to_i

            if (@argument % 2 == 0)
                puts "pair"     
                puts "#{0}"  
                
            elsif (@argument % 2 == 1)
                puts "impair"
                puts "#{1}"  

            else
                puts "Tu ne me la mettra pas à l'envers."    
                puts "#{2}"        
            
            end

        else
            puts "Tu ne me la mettra pas à l'envers."    
            puts "#{3}" 
            puts "#{@argument}"
            
        end
    end
end

if __FILE__ == $0 
    pe = Peer.new

    pe.compare  


end
