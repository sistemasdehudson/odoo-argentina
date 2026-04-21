import logging

_logger = logging.getLogger(__name__)


def migrate(cr, version):
    """
    Pre-migración l10n_ar_ux 19.0.1.8.0
    Elimina xmlids de tags de jurisdicción provincial que ya no existen
    en el código v19. Los tags se crean dinámicamente por l10n_ar_tax.
    Sin este fix Odoo intenta borrar los tags que siguen siendo usados
    por impuestos de retención/percepción y falla por FK constraint.
    """
    _logger.info("l10n_ar_ux pre-migrate: eliminando xmlids de tags de jurisdicción")
    cr.execute("""
        DELETE FROM ir_model_data
        WHERE module = 'l10n_ar_ux'
          AND model = 'account.account.tag'
          AND name LIKE 'tag_tax_jurisdiccion_%'
    """)
    _logger.info(f"  ✓ {cr.rowcount} xmlids de tags de jurisdicción eliminados")