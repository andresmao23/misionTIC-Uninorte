package reto1;

public class Paciente {
    
    private String nombre;
    private String cedula;
    private String naucea, vomito, dolorAbdominal, diarrea, fiebre;

    public Paciente() {
    }

    public Paciente(String nombre, String cedula, String naucea, String vomito, 
            String dolorAbdominal, String diarrea, String fiebre) {
        this.nombre = nombre;
        this.cedula = cedula;
        this.naucea = naucea;
        this.vomito = vomito;
        this.dolorAbdominal = dolorAbdominal;
        this.diarrea = diarrea;
        this.fiebre = fiebre;
    }

    
    public String getDiagnostico(String naucea, String vomito, String dolorAbdominal,
    String diarrea, String fiebre){        
        String diagnostico = "";
        if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Staphylococcus aureus";
                //contDiagnostico1+=1;
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("no")){
                diagnostico = "Bacillus cereus";
                //contDiagnostico2+=1;
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("no")
                    && dolorAbdominal.equalsIgnoreCase("si")
                    && diarrea.equalsIgnoreCase("no")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Taenia saginata";
                //contDiagnostico3+=1;
            }else if(naucea.equalsIgnoreCase("si") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("si")){
                diagnostico = "Norovirus";
                //contDiagnostico4+=1;
            }else if(naucea.equalsIgnoreCase("no") && vomito.equalsIgnoreCase("si")
                    && dolorAbdominal.equalsIgnoreCase("no")
                    && diarrea.equalsIgnoreCase("si")
                    && fiebre.equalsIgnoreCase("no")){
                diagnostico = "Rotavirus";
                //contDiagnostico5+=1;
            }else{
                diagnostico = "Sin diagnostico";
                //contDiagnostico6+=1;
            }            
        return diagnostico;
    }
    

    public void setNombres(String nombres) {
        this.nombre = nombres;
    }

    public void setCedula(String cedula) {
        this.cedula = cedula;
    }

    public void setVomito(String vomito) {
        this.vomito = vomito;
    }

    public void setDolorAbdominal(String dolorAbdominal) {
        this.dolorAbdominal = dolorAbdominal;
    }

    public void setDiarrea(String diarrea) {
        this.diarrea = diarrea;
    }

    public void setFiebre(String fiebre) {
        this.fiebre = fiebre;
    }   

    public String getNombre() {
        return nombre;
    }

    public String getCedula() {
        return cedula;
    }
    
    public String getNaucea() {
        return naucea;
    }

    public String getVomito() {
        return vomito;
    }

    public String getDolorAbdominal() {
        return dolorAbdominal;
    }
    
    public String getDiarrea() {
        return diarrea;
    }

    public String getFiebre() {
        return fiebre;
    }
    
}
