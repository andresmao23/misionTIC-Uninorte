package reto2;
import java.util.Scanner;

public class reto2 {

    public static void main(String[] args) {
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
        
        Scanner input = new Scanner(System.in);
        int n = Integer.parseInt(input.nextLine());
        
        String [] datosPacientes = new String[n];
        for(int i=0;i<datosPacientes.length;i++){
            datosPacientes[i] = input.nextLine();
        }
        
        for(int i=0;i<datosPacientes.length;i++){
            String nombre = datosPacientes[i].split("-")[0];
            String cedula = datosPacientes[i].split("-")[1];
            String naucea = datosPacientes[i].split("-")[2];
            String vomito = datosPacientes[i].split("-")[3];
            String dolorAbdominal = datosPacientes[i].split("-")[4];
            String diarrea = datosPacientes[i].split("-")[5];
            String fiebre = datosPacientes[i].split("-")[6];
            Paciente paciente = new Paciente(nombre, cedula, naucea, vomito, 
                    dolorAbdominal, diarrea, fiebre);
            
            String diagnostico = paciente.diagnosticar(naucea, vomito, 
                    dolorAbdominal, diarrea, fiebre);
            
            if(diagnostico.equalsIgnoreCase("Staphylococcus aureus")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico1+=1;
            }else if(diagnostico.equalsIgnoreCase("Bacillus cereus")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico2+=1;
            }else if(diagnostico.equalsIgnoreCase("Taenia saginata")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico3+=1;
            }else if(diagnostico.equalsIgnoreCase("Norovirus")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico4+=1;
            }else if(diagnostico.equalsIgnoreCase("Rotavirus")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico5+=1;
            }else if(diagnostico.equalsIgnoreCase("Sin diagnostico")){
                System.out.println(paciente.getCedula() + " " + diagnostico);
                contDiagnostico6+=1;
            }            
        }
        
        if(contDiagnostico1>=contDiagnostico2 && contDiagnostico1>=contDiagnostico3
                && contDiagnostico1>=contDiagnostico4 && contDiagnostico1>=contDiagnostico5
                && contDiagnostico1>=contDiagnostico6){
                System.out.println(diagnosticos[0]);
        }else if(contDiagnostico2>=contDiagnostico1 && contDiagnostico2>=contDiagnostico3
                && contDiagnostico2>=contDiagnostico4 && contDiagnostico2>=contDiagnostico5
                && contDiagnostico2>=contDiagnostico6){
                System.out.println(diagnosticos[1]);
        }else if(contDiagnostico3>=contDiagnostico1 && contDiagnostico3>=contDiagnostico2
                && contDiagnostico3>=contDiagnostico4 && contDiagnostico3>=contDiagnostico5
                && contDiagnostico3>=contDiagnostico6){
                System.out.println(diagnosticos[2]);
        }else if(contDiagnostico4>=contDiagnostico1 && contDiagnostico4>=contDiagnostico2
                && contDiagnostico4>=contDiagnostico3 && contDiagnostico4>=contDiagnostico5
                && contDiagnostico4>=contDiagnostico6){
                System.out.println(diagnosticos[3]);
        }else if(contDiagnostico5>=contDiagnostico1 && contDiagnostico5>=contDiagnostico2
                && contDiagnostico5>=contDiagnostico3 && contDiagnostico5>=contDiagnostico4
                && contDiagnostico5>=contDiagnostico6){
                System.out.println(diagnosticos[4]);
        }else if(contDiagnostico6>=contDiagnostico1 && contDiagnostico6>=contDiagnostico2
                    && contDiagnostico6>=contDiagnostico3 && contDiagnostico6>=contDiagnostico4
                && contDiagnostico6>=contDiagnostico5){
                    System.out.println(diagnosticos[5]);
            }
        
        System.out.println(contDiagnostico6);
    }    
}
