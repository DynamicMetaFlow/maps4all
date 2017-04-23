from .. import db
import os


class SiteAttribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    attr_name = db.Column(db.String(100), unique=True)
    value = db.Column(db.String(255))

    @staticmethod
    def get(attr):
        attribute = SiteAttribute.query.filter_by(attr_name=attr).first()
        if attribute is None:
            attribute = SiteAttribute(attr_name=attr)
            if attribute in os.environ:
                attribute.value = os.environ[attribute]
            else:
                attribute.value = ""

            db.session.add(attribute)
            db.session.commit()

        return attribute.value
