enum PermissionLevel{
    ADMIN,DEVELOPER,USER;
}

public class PermissionManager{
    private PermissionLevel mLevel = PermissionLevel.USER;
    public void set(PermissionLevel level){
        this.mLevel = level;
    }
    public String get(){
        return switch (this.mLevel) {
            case USER -> "USER";
            case DEVELOPER -> "DEVELOPER";
            case ADMIN -> "ADMIN";
        };
    }
}