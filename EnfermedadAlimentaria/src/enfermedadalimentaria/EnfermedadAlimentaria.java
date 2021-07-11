/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package enfermedadalimentaria;

import java.util.Scanner;

/**
 * Reto 1	
 * @author mao
 */
public class EnfermedadAlimentaria {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        String [] diagnosticos = {
            "Staphylococcus aureus",
            "Bacillus cereus",
            "Taenia saginata",
            "Norovirus",
            "Rotavirus",
            "Sin diagnostico"
        };
        
        int contDiagnostico1 = 0;
        int contDiagnostico2 = 0;
        int contDiagnostico3 = 0;
        int contDiagnostico4 = 0;
        int contDiagnostico5 = 0;
        int contDiagnostico6 = 0;
        
        //System.out.print("Digite la cantidad de pacientes: ");
        Scanner input = new Scanner(System.in);
        int n = Integer.parseInt(input.nextLine());
        
        String [] datosPacientes = new String[n];
        for(int i=0;i<datosPacientes.length;i++){
            System.out.print("Paciente "+(i+1)+": ");
            datosPacientes[i] = input.nextLine();
        }
        
        for(int i=0;i<datosPacientes.length;i++){
            //System.out.println(datosPacientes[i]);
            String nombre = datosPacientes[i].split("-")[0];
            String cedula = datosPacientes[i].split("-")[1];
            String naucea = datosPacientes[i].split("-")[2];
            String vomito = datosPacientes[i].split("-")[3];
            String dolorAbdominal = datosPacientes[i].split("-")[4];
            String diarrea = datosPacientes[i].split("-")[5];
            String fiebre = datosPacientes[i].split("-")[6];
            
            if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                System.out.println(cedula + " " + diagnosticos[0]);
                contDiagnostico1+=1;
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("no")){
                System.out.println(cedula + " " + diagnosticos[1]);
                contDiagnostico2+=1;
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("no")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("si")){
                System.out.println(cedula + " " + diagnosticos[2]);
                contDiagnostico3+=1;
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                System.out.println(cedula + " " + diagnosticos[3]);
                contDiagnostico4+=1;
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("no")){
                System.out.println(cedula + " " + diagnosticos[4]);
                contDiagnostico5+=1;
            }else{
                System.out.println(cedula + " " + diagnosticos[5]);
                contDiagnostico6+=1;
            }            
        }
        if(contDiagnostico1>=contDiagnostico2 && contDiagnostico1>=contDiagnostico3
                && contDiagnostico1>=contDiagnostico4 && contDiagnostico1>=contDiagnostico5){
                System.out.println(diagnosticos[0]);
        }else if(contDiagnostico2>=contDiagnostico1 && contDiagnostico2>=contDiagnostico3
                && contDiagnostico2>=contDiagnostico4 && contDiagnostico2>=contDiagnostico5){
                System.out.println(diagnosticos[1]);
        }else if(contDiagnostico3>=contDiagnostico1 && contDiagnostico3>=contDiagnostico2
                && contDiagnostico3>=contDiagnostico4 && contDiagnostico3>=contDiagnostico5){
                System.out.println(diagnosticos[2]);
        }else if(contDiagnostico4>=contDiagnostico1 && contDiagnostico4>=contDiagnostico2
                && contDiagnostico4>=contDiagnostico3 && contDiagnostico4>=contDiagnostico5){
                System.out.println(diagnosticos[3]);
        }else if(contDiagnostico5>=contDiagnostico1 && contDiagnostico5>=contDiagnostico2
                && contDiagnostico5>=contDiagnostico3 && contDiagnostico5>=contDiagnostico4){
                System.out.println(diagnosticos[4]);
        }
        System.out.println(contDiagnostico6);
    }    
}
