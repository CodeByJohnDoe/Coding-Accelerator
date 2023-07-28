
class Peer
    attr_accessor   :argument, :numbers, :type


    def compare
    
    @argument   = ARGV[0].to_i
    @type       = ARGV[0] !~ numbers
    puts "#{@argument}"
    puts "#{@type}"


        if (ARGV[0] =~ @numbers ) == nil || (@type == false)
            puts "Tu ne me la mettra pas à l'envers."       
  

        else  
            if (@argument % 2 == 0)
                puts "pair"     
                
            else (@argument % 2 == 1)
                puts "impair"     

            end
        end
    end
end

if __FILE__ == $0 
    pe = Peer.new

    pe.numbers   = /[±]\d/
    pe.compare  
end

--------------------------------------------------------------------------

 # Time :  2 h 

 class Peer
    attr_accessor   :argument, :type

    def contain_number(str)
        str =~ /[0-9]/
    end


    def compare
    
    @argument = ARGV[0].to_i
    puts "#{@argument}"
    @type   = contain_number(ARGV[0])                              
    puts "#{@type}"

        if (@type == nil)
            puts "Tu ne me la mettra pas à l'envers."       
  
        else  
            if (@argument % 2 == 0)
                puts "pair"     
                
            else (@argument % 2 == 1)
                puts "impair"     

            end
        end
    end
end

if __FILE__ == $0 
    pe = Peer.new

    pe.compare  
end
