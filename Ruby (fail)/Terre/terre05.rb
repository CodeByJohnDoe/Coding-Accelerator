
 # Time :  15 min

 class Division
    attr_accessor   :dividend, :divider, :result, :rest
    def division

        @dividend   = ARGV[0].to_i
        @divider    = ARGV[1].to_i

        if (@divider == 0) || (@dividend < @divider) 
            puts "erreur."
        
        else
            @result = @dividend / @divider
            @rest   = @dividend - (@result * @divider)

            puts "résultat : #{@result}"
            puts "reste    : #{@rest}"
        end
    end
end

if __FILE__ == $0 
    dv = Division.new

    dv.division

end
