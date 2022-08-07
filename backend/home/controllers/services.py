from sqlalchemy import desc, asc
from backend.app import db
from backend.models.models_basics import Services, services_schema, service_schema


class ServicesControllers:
    @staticmethod
    def get_all_services():
        return services_schema.dump(Services.query.order_by(desc(Services.id)).all())

    @staticmethod
    def get_services(limit=4):
        return services_schema.dump(Services.query.order_by(asc(Services.time_added)).limit(limit))

    @staticmethod
    def get_service(name):
        return service_schema.jsonify(Services.query.filter_by(name=name).first())

    def add_service(self, name, title, description, icon):
        service = self.get_service(name)
        if service:
            return False
        new_service = Services(
            name=name,
            title=title,
            description=description,
            icon=icon
        )
        db.session.add(new_service)
        db.session.commit()
        return True

    def modify_service(self, name, new_name, title, description, icon):
        service = self.get_service(name)
        if service:
            service.name = new_name
            service.title = title
            service.description = description
            service.icon = icon
            db.session.add(service)
            db.session.commit()
            return True
        return False

    def delete_service(self, name):
        service = self.get_service(name)
        if service:
            db.session.delete(service)
            db.session.commit()
            return True
        return False
