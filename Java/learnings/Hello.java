class Hello
{
    public static void main(String[] args){
        char k = 'a';
        k++;
        System.out.println(k); 
        int a = 257;
        byte b = (byte)a; 
        System.out.println(b);

        int num =2;
        //post increment .First it will assign and then increase
        int result = num++;
        System.err.println(result);
    }
}